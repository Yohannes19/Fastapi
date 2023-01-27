import pandas as pd
import matplotlib.pyplot as plot
from starlette.responses import StreamingResponse
from threading import Thread
from fastapi import FastAPI
app=FastAPI()
url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
  
if __name__ == "__main__":    
    @app.get("/myapi")
    def hello(name=None):
        if name==None:
            text="Hello only"
        else:
            text =" Hello" + name    
        return text

    @app.get("/getcsv")
    def csvreader():
    
        cs=pd.read_csv(url)
        
        return cs

    @app.get("/plotdata")
    def dataplot():
        pl= pd.read_csv(url)
        plot.scatter(pl['sepal_length'],pl['sepal_width'])
        plot.savefig('pl.png')
        file =open('p1.png',mode="rb")
        
        return StreamingResponse(file, media_type="image/png")
        
