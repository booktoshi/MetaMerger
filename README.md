# NR-MetaMerger
TheNodeRunners MetaMerger

This script works with the metadata trait json sheets that are provided to you when you use the Hashlips Art Generator Template to generate your metadata and/or metaddata and artwork. You must have been provided the trait sheets that hashlips generates when used. Inscriptions must be minted to a fresh wallet in sequential order ex. 1,2,4,5,6,7,8,9...

~Create new folder somewhere easy to find;
~Create a 'traits' and 'inscription' folder inside of the new folder you just created;
~Go to this telegram bot https://t.ne/noderunner_tool_bot;
~Start the bot and drop the wallet address of the wallet to where you minted the doginals too (fresh wallet as described above);
~Download the provided inscription ID json file save that file into the 'inscription' folder you created above;
~Take the hashlips generated trait cards provided to you, and copy (ctrl + c) + paste (ctrl + v) into the 'traits' folder created above;
~Now go to Visual Code program, open it, and select 'Open' under the 'START' section;
~Navigate to where you saved your new folder created earlier, press the folder once, and then press open;
~Once the MetaMerger script folder is open, click terminal at the top of the screen and start a 'New Terminal';
~In the terminal window below, run the command python3 merge_traits.py;
~Input the mint wallet address and add .json to end of the wallet address;
~The script will ask you if you want to switch/replace any ID numbers to match the sequential ordering of the inscriptions. The script does this due to potential corrupt files that may be skipped while using the auto-inscriber method;
~For the replacement of IDs due to corrupt files being skipped you must enter the greater number first of the inscription that you would like to switch out with a lower number. So, if #100 was skipped due to corruption and you ended up inscribing #100 at the end of the run at #400, then you would simply command the bot to replace #400 inscription with #100 inscription in the merged metadata file ex: "400 100"
~Once you have switched out all necessary IDs to place them in the proper order, the script will then ask you if you are done - input q;
~The script will then create you a perfectly formatted OrdinalsWallet JSON file with the proper Insciription ID numbers and the proper MetaData fields inputted. 

Please Watch this Step by Step Video: 

~Booktoshi
