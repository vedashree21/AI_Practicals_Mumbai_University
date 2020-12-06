import math

def activate (weights,inputs):
	activation=weights[-1]		
	for i in range (len(weights)-1):		
		activation+=weights[i]*inputs[i]
	return activation

def transfer(activation):		
	return 1.0/(1.0+math.e**(-activation))

def forward_propogation(network,row):		
	inputs=row
	for layer in network:	
		new_input=[]
		for neurons in layer:
			activation=activate(neurons['weights'],inputs)
			neurons['output']=transfer(activation)
			print("The neurons are: "+str(neurons))		
			new_input.append(neurons['output'])
		inputs=new_input
		print(inputs)
	return inputs

network=[[{'weights':[0.12436424411240122,0.847433,0.587687587]}],[{'weights':[0.45345234235435,0.2542352342345]}],[{'weights':[0.453452349765,0.254982345]}]]
row=[1,0,None]
output=forward_propogation(network,row)
print("The output is:"+str(output))