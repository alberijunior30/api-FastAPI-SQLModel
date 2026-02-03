from sqlmodel import SQLModel

from core.database import engine


async def create_tables() -> None:
    import models.__all_models
    print('Criando as tabelas no Banco de Dados...')

    try:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all) #limpar o banco, cuidado!!
            await conn.run_sync(SQLModel.metadata.create_all)
        print("Tabelas criadas com Sucesso!!")

    except Exception as e:
        print(f"Algo deu errado na criação da Tabela!: {e}")



if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())