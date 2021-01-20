# pixiv-scraper
### download images from pixiv

a scraper to download images from [pixiv](https://pixiv.net).
downloads images in the original resolutions, including images in manga and ugoira, from specified users straight to the specified download directory.

### notes
- if you want to download R18 content, you need to change the viewing restrictions in your pixiv account's user settings

### instructions
- install python3 3.6+
- edit the config.json in the data folder manually
	- `save_directory` to the directory you want to save to
	- `users` to the user id shown in the url
	- the username and password fields should be straightforward

### usage
```
$ python3 main.py -h


usage: main.py [-h] [-f FILE] [-l] [-u USERNAME] [-p PASSWORD] [-s SAVE_DIR]
               [-t THREADS]
               {artwork,bookmark,ranking} ...

positional arguments:
  {artwork,bookmark,ranking}
    artwork             download artworks from user IDs specified in "users"
                        field
    bookmark            download bookmark artworks from user IDs specified in
                        "bookmarks" field
    ranking             download top N ranking artworks based on given
                        conditions

optional arguments:
  -h, --help            show this help message and exit
  -f FILE               load file for this instance (default:
                        data/config.json)
  -l                    list current settings
  -u USERNAME           set username
  -p PASSWORD           set password
  -s SAVE_DIR           set save directory path
  -t THREADS            set number of threads for this instance
```

```
$ python3 main.py artwork -h

usage: main.py artwork [-h] [-a  [ID ...]] [-d all [ID ...]] [-c all [ID ...]]

optional arguments:
  -h, --help       show this help message and exit
  -a  [ID ...]     add user IDs
  -d all [ID ...]  delete user IDs and their directories
  -c all [ID ...]  clear directories of user IDs
```

```
$ python3 main.py ranking -h

usage: main.py ranking [-h] -m MODE -c CONTENT -d YYYYMMDD [-n N]

optional arguments:
  -h, --help   show this help message and exit
  -m MODE      modes: {daily, weekly, monthly, rookie, original, male, female,
               daily_r18, weekly_r18, male_r18, female_r18}
  -c CONTENT   contents: {all, illust, ugoira, manga}
  -d YYYYMMDD  date
  -n N         get top N artworks (default: 20)
```

### examples

download artworks from user ids stored in the config file; updates users' artworks if directories already exist

```
python3 main.py artwork
```

download bookmarked artworks from user ids stored in the config; updates users' artworks if directories already exit

```
python3 main.py bookmark
```

delete user ids and their directories (ids in users field and artwork directories), then download artworks for remaining IDs in config file

```
python3 main.py artwork -d 26690900
```

add user ids (ids in bookmarks field) then download bookmark artworks for newly add ids + ids in config file

```
python main.py bookmark -a 26690900
```
