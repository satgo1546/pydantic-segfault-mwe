import threading
import pydantic.version
from pydantic import BaseModel
print(pydantic.version.version_info(), flush=True)
class MyModel(BaseModel):
    a: str
threading.Thread(target=lambda: print(MyModel.model_validate_json('{"a":"ok"}'))).start()
