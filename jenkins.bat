cd C:\Users\vladosnasos\Desktop\Code\QA\SOFTMETTEST
C:\Python312\python.exe -m pip install -r C:\Users\vladosnasos\Desktop\Code\QA\ve\requirements.txt
git init
git config --global user.email "bezzzubkovlad@gmail.com"
git config --global user.name "vladosnasos"
git remote add origin https://github.com/vladosnasos/SOFTMETTEST.git
git branch -M main
pre-commit install
git add ./.pre-commit-config.yaml
git add C:\Users\vladosnasos\Desktop\Code\QA\SOFTMETTEST\main.py
git add C:\Users\vladosnasos\Desktop\Code\QA\SOFTMETTEST\test_main.py
git commit -m "testing pre-commits"
