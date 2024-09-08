#!/usr/bin/env python
# coding: utf-8

# In[69]:


# Continuation of CNOT ID1 is CNOT gate reverse, here we get same output
# refer to http://localhost:8888/notebooks/CNOT%20ID1.ipynb
# https://www.youtube.com/watch?v=uNrPJ3_Mttc
from qiskit import* 
from qiskit.visualization import visualize_transition, plot_histogram, plot_bloch_multivector


# In[70]:


#import qiskit_textbook and display the unitary matrix
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex


# In[71]:


# Create a quantum Circuit with 1 qubits
qc= QuantumCircuit(1)
state = Statevector.from_instruction(qc)


# In[72]:


#Draw the circuit
#qc.draw()
qc.draw('mpl')


# In[73]:


#draw the initial bloch sphere
state.draw('Bloch', title = 'Initial Bloch sphere representation of state vector')


# In[74]:


# draw the latec
state.draw('latex', prefix= '\\text{Statevector} \\psi\\rangle = ')


# In[75]:


# Observe above initial state before applying the gate
#Apply the X/Y/Z gates in the below and extract the output in different forms like 'latex/bloch/array' gate Gate
qc.x(0)
state = Statevector.from_instruction(qc)
state.draw('latex', prefix= '\\text{Statevector} |\\psi\\rangle = ')


# In[76]:


#Draw the circuit
#qc.draw()
qc.draw('mpl')


# In[77]:


state.draw('text', prefix= '\\text{Statevector} |\\psi\\rangle = ')


# In[78]:


#draw the initial bloch sphere
state.draw('Bloch', title = 'Bloch sphere with X or Y or Z gate based on above selection')


# In[79]:


#simulator = Aer.get_backend('qasm_simulator')
#result = execute(qc,backend=simulator, shots=1).result()
#counts = out.get_counts()
#print(counts)


# In[68]:


plot_histogram([counts])


# In[ ]:




