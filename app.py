import numpy as np
import random 
import operator
import itertools
import streamlit as st

operaciones = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': lambda x, y: x / y if y != 0 else None  
}

def aplicar_operaciones(nums, ops):
    resultado = nums[0]
    for i in range(3): 
        resultado = operaciones[ops[i]](resultado, nums[i + 1])
        if resultado is None:  
            return None
    return resultado

def generar_resultados(valores):
    resultados = []
    operaciones_usadas = []
    
    for nums in itertools.permutations(valores):
        for ops in itertools.product(operaciones.keys(), repeat=3):
            resultado = aplicar_operaciones(nums, ops)
            if resultado is not None and resultado % 1 == 0:
                operacion_str = f"{nums[0]}"
                for i in range(3):
                    operacion_str += f" {ops[i]} {nums[i + 1]}"
                resultados.append(resultado)
                operaciones_usadas.append(operacion_str)
    
    return resultados, operaciones_usadas

st.title("Calculadora de Operaciones")
st.write("Ingrese 4 números y el número objetivo:")

numeros = []
for i in range(4):
    numero = st.number_input(f"Número {i+1}", key=f"num{i}", min_value=0)
    numeros.append(numero)

objetivo = st.number_input("Número objetivo", min_value=0)

if st.button("Calcular"):
    resultados, ops = generar_resultados(numeros)
    encontrado = False
    for i in range(len(resultados)):
        if resultados[i] == objetivo:
            st.write(f"Operación encontrada: {ops[i]}")
            encontrado = True
            break
    if not encontrado:
        st.write("No se encontró ninguna operación que coincida con el objetivo.")

