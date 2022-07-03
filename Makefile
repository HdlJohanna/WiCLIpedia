forge:
  pyinstaller --onefile wiclipedia.py
  gzip ./manpage.7
  mv ./manpage.7.gz ./wiclipedia.7.gz
  sudo mv ./wiclipedia.7.gz /usr/share/man/man7
