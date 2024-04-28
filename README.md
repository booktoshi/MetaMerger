<div align="center">

# <span style="color:#013db7;">TheNodeRunners MetaMerger</span>

</div>

**The NodeRunner MetaMerger** is developed to work with a fresh inscription wallet where the inscriber is sending the inscriptions to a brand new wallet and the inscriptions are **being minted in sequential ID # order as provided by Hashlip Art Generator for images and metadata sheets.** 

This script works with the metadata trait JSON sheets provided when using the **Hashlips Art Generator Template** https://github.com/hashlips-lab/art-engine-template to generate your metadata and/or artwork. You must have the trait sheets that Hashlips generates when used. This is also assuming that you are using one of the auto-inscribers created by https://github.com/martinseeger2002 | https://github.com/martinseeger2002/dogcoin_ordinal_auto_inscriber

### Pre-Requisite 1: First Mint your Collection using https://github.com/booktoshi/doginals **with** https://github.com/martinseeger2002/dogcoin_ordinal_auto_inscriber
### Pre-Requisite 2: Download this folder and save it in a easy-to-find place on your computer https://github.com/booktoshi/NR-MetaMerger/archive/refs/heads/main.zip
### Pre-Requisite 3: Python3 https://realpython.com/installing-python/
### Pre-Requisite 4: Hashlips https://github.com/hashlips-lab/art-engine-template 
### Instructions

1. **Setup Environment**
   - Create a new folder in an easy-to-find location.
   - Inside this new folder, create two subfolders: `traits` and `inscriptions` (included if downloading this repo).
   
2. **Prepare Data**
   - Visit the Telegram bot [NodeRunner Tool Bot](https://t.me/noderunner_tool_bot).
   - Start the bot and enter the wallet address where you minted the Doginals (must be a fresh wallet minted in sequential order 1,2,3,4,5,6,7,8,9).
   - Download the provided inscription ID JSON file and save it into the 'inscriptions' folder.

3. **Execution**
   - Open **Visual Studio Code** and select `Open` under the `START` section.
   - Navigate to your newly created folder, select it (press once!), and then click `Open`.
   - Open a new terminal by selecting `Terminal` at the top of the screen and then select > `New Terminal` from the drop down.
   - Run the command:
     ```bash
     python3 merge_traits.py
     ```
   - Follow the on-screen instructions to input the mint wallet address and adjust ID numbers as necessary. This will need to be done if you are using the auto-insciber and the auto-inscriber runs into a corrupt file. The auto-inscriber will skip the corrupt file and go to the next file. As a result, you need to find that missed inscription and inscribe that at the end of the mint.
   - The script will ask you if you want to replace any inscription ID numbers, if you need to replace any inscription ID numbers due to the auto-inscriber skipping files, you will commmand the script the larger number first and then the smaller number second. 

### Example: (do not copy)   
```
Please enter the index to switch to: (FROM --> TO), press q to end: 366 157
Switching 366 with 157, all the index starting from 157 till 366 will be shifted by 1
Please enter the index to switch to: (FROM --> TO), press q to end: 653 652
Switching 652 with 653, all the index starting from 653 till 652 will be shifted by 1
Please enter the index to switch to: (FROM --> TO), press q to end: 661 660
Switching 660 with 661, all the index starting from 661 till 660 will be shifted by 1
Please enter the index to switch to: (FROM --> TO), press q to end: q
```
   **When you replace any inscriptions numbers the script will automatically re-org the list to make sure that the ID Name #s are in order so that when you run the merge_traits.py script the numbers match the hashlips trait sheets which directly correalate to the # in the collection.**

4. **Finalizing**
   - After replacing IDs and ensuring correct sequential order, type `q` for the script to finalize and populate a json.
   - The script will generate a perfectly formatted **OrdinalsWallet JSON file** with correct Inscription ID numbers and Metadata fields inputted.

### <span style="color:#e3e5e2;">Additional Resources</span>

- **Please Watch this Step by Step Video:**
  - [Booktoshi Tutorial](Coming Soon https://www.youtube.com/channel/UCg7Ch2vwoQ2-hM0eNya8q6g)

### <span style="color:#000000;">Contributing</span>

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated, {nodeRunners}**.

---

<div align="center" style="background-color:#c9f001; color:#013db7; padding:10px; border-radius:8px;">
<strong>Contact Information:</strong> For further assistance or queries, please contact our support team https://discord.gg/6z2bek9Yf7.
</div>

