import json
from fastapi import FastAPI, HTTPException
with open("menu.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()

@app.get('/')
def root():
    return{'Menu' : "Item"}

@app.get('/menu/{item_id}')
async def read_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )


@app.put('/menu/{item_id}')
async def read_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

@app.get('/menu')
async def read_all_menu():
        return data

@app.post('/menu')
async def post_menu(name:str):
    id=1
    if(len(data["menu"])>0):
        id=data["menu"][len(data["menu"])-1]["id"]+1
    new_data={'id':id,'nama':name}
    data['menu'].append(dict(new_data))
    read_file.close()
    with open("menu.json", "w") as write_file:
        json.dump(data,write_file, indent=4)
    write_file.close()

    return (new_data)

@app.put('/menu/{item_id}')
async def update_menu(item_id: int, name:str):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            menu_item['name']=name
            with open("menu.json", "w") as write_file:  
                json.dump(data,write_file, indent=4)
            write_file.close()

        return{"message": "Data updated successfully"}


@app.delete('/menu/{item_id}')
async def update_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            data['menu'].remove(menu_item)
            with open("menu.json","w") as write_file:
                json.dump(data,write_file,indent=4)
            write_file.close()   

    return{"message":"Data deleted successfully"}
