import concurrent.futures
import multiprocessing
import requests
def downloadFile(url,name):
    response=requests.get(url)
    print(f'started downloading {name}')
    open(f'gg1/file{name}.jpg',"wb").write(response.content)
    print(f"Finished downloading {name}")
    # if __name__=="__main__":
    url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeautiful%2F&psig=AOvVaw14wYw9zabZqBwW1cNnmNtn&ust=1743438623591000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMiV_ZCdsowDFQAAAAAdAAAAABAE"
    pros=[]
     # for i in range(5000):
     #    # downloadFile(url,i)
     #    p=multiprocessing.Process(target=downloadFile,args=[url,i])
     #    p.start()
     #    pros.append(p)
     # for p in pros:
     #    p.join()
with concurrent.futures.ProcessPoolExecutor() as executor:
    l1=[url for url in range(50)]
    l2=[i for i in range(50)]
    results = executor.map(downloadFile,l1,l2)
    for r in results:
     print(r)