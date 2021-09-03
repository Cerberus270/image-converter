# File converter for Discord stickers

## History
One day I wanted to add new stickers to my Discord server, so I downloaded the stickers that I use on WhatsApp from my browser and the ones I use there from Telegram, and they were downloaded in [.webp](https://en.wikipedia.org/wiki/WebP) format, and when trying to upload them to Discord, it did not recognize it as a valid format, so I looked for an online convert and while the file was uploaded, I thought that this task could be automated with Python, so I decided to create this little program


## Requirements
The only external library require is PIL (Pillow).

check [Pillow](https://pypi.org/project/Pillow/)
```bash
pip install Pillow
```

## Usage

### Many Files
Search and convert all webp and png files to jpeg, parameter --path may be absolute path, --type is the files extensions to search
--output flag is the type file that you want to be saved(note: jpg must be as jpeg).
```bash
python .\test2.py -p C:\Users\Cerberus\Documents\Repositorios\discord-stickers\htest-files -t webp,png -o jpeg
```

### Only one file

Search and convert only one file, given a path that is a file wiht a valid extension, --path flag is required and --out
```bash
python .\converter.py -p C:\Users\Cerberus\Documents\Repositorios\discordStickers\test-files\pngTest1.png  -o jpeg
```

The program has been tested in Windows 10 and Kubuntu 20.04

All type files have not been tested yet, the list of image formats is provided by PIL.

There are an exception if the path given is from a folder an --type is not specified.

### Contributing

It is a simple program I used to practice arguments and system libraries, if you want to make a change or improve it, all pull request are welcome, the next step is to convert it into a bash accessible program for Linux systems.

For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

If you find a bug, feel free to fix it or let me know.



## License

I am still a developer in training, I will investigate more about it later.
