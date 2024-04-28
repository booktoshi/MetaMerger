import os
import json


class DataMerger:
    """
    DataMerger class

    Merge inscription data with corresponding traits data.

    Attributes:
        inscription_folder (str): The folder path where the inscription data is stored. Default is "inscriptions".
        merged_folder (str): The folder path where the merged data is saved. Default is "complete_data".
        traits_folder (str): The folder path where the trait data is stored. Default is "traits".
        Address_input_message (str): The message prompt for entering the address of the inscriptions' folder.

    """

    def __init__(self):
        """
        Initialize DataMerger object
        """
        self.inscription_folder = "inscriptions"
        self.merged_folder = "complete_data"
        self.traits_folder = "traits"
        self.address_input_message = """Note: The address should be the same as the filename of the inscriptions folder.
        Enter the address: """

    def create_directory(self) -> None:
        """
        Creates directory for merged data if it does not exist
        """
        if not os.path.exists(self.merged_folder):
            os.makedirs(self.merged_folder)
            print("Created directory for merged data.")

    def get_address(self) -> str:
        """
        Get the address of the inscription files.
        If only one file, return the address of the file, otherwise ask for the input
        :return: Address/the filename of the inscriptions folder
        """
        if len(os.listdir(self.inscription_folder)) == 1:
            return os.listdir(self.inscription_folder)[0]

        return input(self.address_input_message)

    def load_inscriptions(self, address: str) -> list[dict]:
        """
        Load inscriptions from a specified file.

        :param address: The address of the file containing inscription data.
        :type address: Wallet address of the inscriptions
        :return: A list of inscription ids loaded from the file.
        :rtype: List
        """
        inscriptions_file = os.path.join(self.inscription_folder, address)
        inscription_ids = json.load(open(inscriptions_file))
        return inscription_ids

    def load_traits(self) -> list[dict]:
        """
        Load all traits from all files in the traits folder
        :return: List of dictionaries of traits
        """
        merged_traits = [
            json.load(open(os.path.join(self.traits_folder, file)))
            for file in os.listdir(self.traits_folder)
        ]
        return merged_traits

    @staticmethod
    def merge_data(inscription_ids: list[dict], merged_traits: list[dict]) -> list[dict]:
        """
        Merge inscriptions ids and traits
        :param inscription_ids: dictionary of an Inscription ids
        :param merged_traits: list of traits
        :return: Complete data as a list of dictionaries
        """
        complete_data = []
        for idx, (inscription, traits) in enumerate(zip(inscription_ids, merged_traits)):
            inscription["meta"] = traits
            complete_data.append(inscription)

        if len(merged_traits) != len(inscription_ids):
            print(
                f"Warning: The number of inscriptions ({len(inscription_ids)}) does not match the number of traits ({len(merged_traits)}), "
                f"please check the data. Merging the starting {min(len(inscription_ids), len(merged_traits))} inscriptions.")

        return complete_data

    def reorder_inscriptions(self, address: str, from_idx: int, to_idx: int):
        """
        Reorder the inscriptions by moving the inscription at from_idx to to_idx
        :param address: Wallet address
        :param from_idx: IDx of the inscription to move
        :param to_idx: IDx to move the inscription to
        :return: None, update the inscriptions file
        """
        from_idx -= 1
        to_idx -= 1

        inscriptions = self.load_inscriptions(address)
        inscription_to_move = inscriptions.pop(from_idx)
        inscription_to_move["meta"]["name"] = str(to_idx + 1)

        # Insert moved item to correct place
        inscriptions.insert(to_idx, inscription_to_move)

        for idx in range(len(inscriptions)):
            if to_idx < idx <= from_idx:
                inscriptions[idx]["meta"]["name"] = str(idx + 1)

        inscriptions.sort(key=lambda x: int(x["meta"]["name"]))
        self.update_inscriptions(address, inscriptions)

    def fix_inscriptions(self, address: str):
        """
        Continuously prompt user to switch the position of two indices in the inscriptions until user stops
        :param address: the Wallet address of the inscriptions
        :return: None
        """
        while True:
            try:
                user_input = input("Please enter the index to switch to: (FROM --> TO), press q to end: ")
                if user_input in ["q", "Q"]:
                    print("Exiting the program")
                    break
                user_input = user_input.split(" ")
                if len(user_input) != 2:
                    print("Please enter two indices separated by space")
                    continue

                from_idx, to_idx = user_input[0], user_input[1]
                print(
                    f"Switching {from_idx} with {to_idx}, all the index starting from {to_idx} till {from_idx} will be shifted by 1")
                self.reorder_inscriptions(address, int(from_idx), int(to_idx))
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

    def update_inscriptions(self, address: str, inscriptions: list[dict]) -> None:
        """
        Update the inscriptions file with the new inscriptions
        :param address: Address of the file where to save the data
        :param inscriptions: List of inscriptions to be saved
        """
        with open(os.path.join(self.inscription_folder, address), "w") as f:
            json.dump(inscriptions, f)

    def save_data(self, complete_data: list[dict], address: str) -> None:
        """
        Save the complete merged data to the merged directory
        :param complete_data: Merged data to be saved
        :param address: Address of the file where to save the data
        """
        print(complete_data)
        complete_data.sort(key=lambda x: int(x["meta"]["name"].split("#")[1]))
        with open(os.path.join(self.merged_folder, address), "w") as f:
            json.dump(complete_data, f)

    def run(self) -> None:
        """
        Main function to run the data merging operation
        """
        print("Starting the data merging process...")
        self.create_directory()
        address = self.get_address()
        user_input = input("Do you want to fix the order of inscriptions? Y/n ")
        if user_input not in ["n", "N"]:
            self.fix_inscriptions(address)
        inscription_ids = self.load_inscriptions(address)
        merged_traits = self.load_traits()
        complete_data = self.merge_data(inscription_ids, merged_traits)
        self.save_data(complete_data, address)

    def dry_run(self):
        with open(os.path.join(self.merged_folder, self.get_address()), "r") as f:
            complete_file = json.load(f)
            ids = [data["meta"]["name"].split("#")[1] for data in complete_file]
            print(ids)


if __name__ == '__main__':
    merger = DataMerger()
    merger.run()
