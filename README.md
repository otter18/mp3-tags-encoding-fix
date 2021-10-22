# MP3 tags encoding fix tool

## Usage
- `python3 main.py {dir_path}`

## Example
```shell
% python3.9 main.py .
-------------------- test.mp3 --------------------
Was: {'album': ['ÀÐÄÈÑ www.ardisbook.ru'], 'copyright': ['© ÀÐÄÈÑ / Art Dictation Studio\x99, 2008'], 'title': ['Предисловие'], 'artist': ['Íàïîëåîí Õèëë'], 'albumartist': ['Íàïîëåîí Õèëë'], 'tracknumber': ['002'], 'genre': ['Àóäèîêíèãà'], 'date': ['2008']}
Now: {'album': ['АРДИС www.ardisbook.ru'], 'copyright': ['© АРДИС / Art Dictation Studio™, 2008'], 'title': ['Предисловие'], 'artist': ['Наполеон Хилл'], 'albumartist': ['Наполеон Хилл'], 'tracknumber': ['002'], 'genre': ['Аудиокнига'], 'date': ['2008']}
--------------------------------------------------
```