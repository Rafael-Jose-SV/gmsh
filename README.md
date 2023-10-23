# gmsh

### bibliotecas utilizadas:

- gmsh
- FastAPI

### como rodar?

#### para criar a imagem docker: 

```shell
docker build -t gmsh .
```

#### para rodar localmente:

baixe as dependencias:

```shell
pip install gmsh
pip install fastapi
pip install "uvicorn[standard]"
```

rode o comando:

```shell
uvicorn app.main:app --reload
```