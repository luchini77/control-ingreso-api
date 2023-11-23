import uvicorn


from api.app import create_app

api = create_app()


# if __name__=="__main__":
#     uvicorn.run("main:api",host="0.0.0.0",port=8080,reload=True)