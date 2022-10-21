1. CLONE OU FAÇA DOWNLOAD DESTE REPOSITORIO;	

2.INSTALLE E ATIVE UM AMBIENTE VIRTUAL USANDO:	

  WINDOWNS:	
	
    python -m venv env	
		
    cd venv/scripts	
		
    activate	
  LINUX :	
	
    pip install virtualenv venv
    source /venv/bin/activate/	
		
3.COM SEU AMBIENTE ATIVO, ENTRE NA PASTA QUE ESTÁ O PROJETO E  INSTALE AS DEPENDENCIAS:	

  cd teste
  pip install requirements.txt	
	
4.INICIE O SERVIDOR	

  python manage.py makemigrations (verifica se tem modificações a serem lançadas no banco de dados)
  python manage.py migrate (migrando tabelas no banco de dados)
  python manage.py runserver (iniciando o servidor)	
	
5. NAVEGUE PELO IP LOCAL: 127.0.0.1
