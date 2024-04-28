<div align="center">

# <span style="color:#013db7;">NR-MetaMerger</span>
## <span style="color:#c9f001;">TheNodeRunners MetaMerger</span>

</div>

This script works with the metadata trait JSON sheets provided when using the **Hashlips Art Generator Template** to generate your metadata and/or artwork. You must have the trait sheets that Hashlips generates when used.

### Pre-Requisites: Python3
### Instructions

1. **Setup Environment**
   - Create a new folder in an easy-to-find location.
   - Inside this new folder, create two subfolders: `traits` and `inscription`.
   
2. **Prepare Data**
   - Visit the Telegram bot [NodeRunner Tool Bot](https://t.me/noderunner_tool_bot).
   - Start the bot and enter the wallet address where you minted the originals (must be a fresh wallet as described).
   - Download the provided inscription ID JSON file and save it into the 'inscription' folder.

3. **Execution**
   - Open **Visual Studio Code** and select `Open` under the `START` section.
   - Navigate to your newly created folder, select it, and then click `Open`.
   - Open a new terminal by selecting `Terminal` > `New Terminal` from the top menu.
   - Run the command:
     ```bash
     python3 merge_traits.py
     ```
   - Follow the on-screen instructions to input the mint wallet address and adjust ID numbers as necessary.

4. **Finalizing**
   - After replacing IDs and ensuring correct sequential order, type `q` to quit.
   - The script will generate a perfectly formatted **OrdinalsWallet JSON file** with correct Inscription ID numbers and Metadata fields.

### <span style="color:#e3e5e2;">Additional Resources</span>

- **Please Watch this Step by Step Video:**
  - [Booktoshi Tutorial]([https://youtube.com](https://www.youtube.com/channel/UCg7Ch2vwoQ2-hM0eNya8q6g))

### <span style="color:#000000;">Contributing</span>

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

---

<div align="center" style="background-color:#c9f001; color:#013db7; padding:10px; border-radius:8px;">
<strong>Contact Information:</strong> For further assistance or queries, please contact our support team.
</div>

