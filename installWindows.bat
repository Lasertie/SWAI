@echo off
echo Installation des dependances...

REM Assurez-vous que python est installé
python --version
if errorlevel 1 (
  echo Python n'est pas installe. Installation...
  curl https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe -o python-3.9.5-amd64.exe
  python-3.9.5-amd64.exe
  REM Demande à l'utilisateur si il veut supprimer le fichier d'installation
  echo Voulez-vous supprimer le fichier d'installation ? (y/n)
  set /p delete=
  if %delete% == y (
    del python-3.9.5-amd64.exe
    echo Fichier supprime.
  ) else (
    echo D accord, je le garde.
  )
  echo Installation terminee.
)

REM Assurez-vous que pip est installé
python -m pip --version
if errorlevel 1 (
  echo pip n'est pas installe. Installation...
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py
  REM Demande à l'utilisateur si il veut supprimer le fichier d'installation
  echo Voulez-vous supprimer le fichier d'installation ? (y/n)
  set /p delete=
  if %delete% == y (
    del get-pip.py
    echo Fichier supprime.
  ) else (
    echo D accord, je le garde.
  )
  echo Installation terminee.
)

REM Installez les dépendances à partir de requirements.txt
echo Installation des dependances avec pip...
python -m pip install -r requirements.txt

echo Installation terminee.
echo Pour plus d'informations, consultez le fichier README.md.
REM On demande à l'utilisateur si il veut aller a README.md
echo Voulez-vous ouvrir le fichier README.md ? (y/n)
set /p open=
if %open% == y (
  start README.md
)
else (
  echo D accord, je ne l ouvrirai pas.
)
REM Appuyez sur une touche pour fermer la fenêtre
pause >nul
```