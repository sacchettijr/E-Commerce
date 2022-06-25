# Projeto de E-Commerce

## Descrição
Este projeto é apenas para fins educativos e treinamento de habilidades dos cursos de Django. 

## Instalação


* #### Windows

1. Crie uma máquina virtual e ative
```
python -m venv venv
cd venv/Scripts
activate
cd ../..
```

2. Instale as dependencias
```
pip install -r requirements.txt
```

3. Carregue o banco de dados e as migrações
```
python manage.py makemigrations
python manage.py migrate
```

5. Carregue os dados iniciais da aplicação
```

run_fixtures.bat

```


5. Coloque o site no ar.
```
python manage.py runserver
```