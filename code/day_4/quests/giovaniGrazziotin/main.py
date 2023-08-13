from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi
from models import Curso
from database import engine, Base, get_db
from repositories import CursoRepository
from schemas import CursoRequest, CursoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/api/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def create(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save(db, Curso(**request.dict()))
    return CursoResponse.from_orm(curso)


@app.get("/api/cursos", response_model=list[CursoResponse])
def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_all(db)
    return [CursoResponse.from_orm(curso) for curso in cursos]


@app.get("/api/cursos/{id}", response_model=list[CursoResponse])
def find_by_id(id: int, db: Session = Depends(get_db)):
    curso = CursoRepository.find_by_id(db, id)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso nao encontrado!")
    else:
        return [CursoResponse.from_orm(curso)]


@app.delete("/api/cursos/{id}", response_model=list[CursoResponse])
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if CursoRepository.exists_by_id(db, id) is False:
        raise HTTPException(status_code=404, detail="Curso nao encontrado!")
    else:
        CursoRepository.delete_by_id(db, id)
        raise HTTPException(status_code=204, detail="Curso deletado!")


@app.put("/api/cursos/{id}", response_model=list[CursoResponse])
def update_by_id(id: int, request: CursoRequest, db: Session = Depends(get_db)):
    if CursoRepository.exists_by_id(db, id) is False:
        raise HTTPException(status_code=404, detail="Curso nao encontrado!")
    else:
        curso = CursoRepository.save(db, Curso(id=id, **request.dict()))
        return [CursoResponse.from_orm(curso)]


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Ambiente Virtual de Aprendizagem",
        version="1.0.0",
        summary="Alunos EAD",
        description="Sistema de Ambiente Virtual de Aprendizagem para auxiliar alunos 100% EAD",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
