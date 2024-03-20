## Some description

This is a test project, where you can isolated-ly test the streamlit problem.    
In this project there is only virtual environment, which has streamlit inside of it and a streamlit file with some code in it.  

## Instructions:

So to run the program, you need to do some things:

1. Clone this repository and be syre that everything is cloned well.
2. Then enter the virtual environment through the ```myvenv\Scripts\activate```line.
3. After that - run this command: ```streamlit run streamlit_ui.py```.
4. To quit the environment use command ```deactivate```.

The main problem for me is the traceback i get for every try i run this file:

```
2024-03-20 18:49:35.289 Uncaught exception
Traceback (most recent call last):
  File "C:\Users\Massimo\PycharmProjects\Streamlit_test\myvenv\lib\site-packages\tornado\http1connection.py", line 276, in _read_message
    delegate.finish()
  File "C:\Users\Massimo\PycharmProjects\Streamlit_test\myvenv\lib\site-packages\tornado\routing.py", line 268, in finish
    self.delegate.finish()
  File "C:\Users\Massimo\PycharmProjects\Streamlit_test\myvenv\lib\site-packages\tornado\web.py", line 2399, in finish
    self.execute()
  File "C:\Users\Massimo\PycharmProjects\Streamlit_test\myvenv\lib\site-packages\tornado\web.py", line 2421, in execute
    self.handler = self.handler_class(
  File "C:\Users\Massimo\PycharmProjects\Streamlit_test\myvenv\lib\site-packages\tornado\websocket.py", line 220, in __init__
    super().__init__(application, request, **kwargs)
  File "C:\Users\Massimo\PycharmProjects\Streamlit_test\myvenv\lib\site-packages\tornado\web.py", line 214, in __init__
    super().__init__()
  File "C:\Users\Massimo\AppData\Local\Programs\Python\Python310\lib\typing.py", line 1422, in _no_init_or_replace_init
    cls.__init__(self, *args, **kwargs)
TypeError: WebSocketHandler.__init__() missing 2 required positional arguments: 'application' and 'request'
```

