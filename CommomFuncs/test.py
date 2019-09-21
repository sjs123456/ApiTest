scope = {}
scope['x'] = 1
scope['y'] = 2
print(eval('x+y', scope))

scope = {}
exec("x=2" in scope)
eval("x*x", scope)