import tkinter as tk
from tkinter import ttk, messagebox

def logica_not(valor):
    return 1 - valor

def logica_and(var1, var2):
    return var1 & var2

def logica_or(var1, var2):
    return var1 | var2

class LogicSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Logica Not Or And")
        
        self.b1 = tk.IntVar(value=0)
        self.b2 = tk.IntVar(value=0)
        self.b3 = tk.IntVar(value=0)
        
        self.values = {"b1": 0, "b2": 0, "b3": 0}
        
        self.operations = []
        
        self.operation_counter = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        frame_bits = ttk.LabelFrame(self.root, text="Bits de Entrada", padding=10)
        frame_bits.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        ttk.Label(frame_bits, text="b1:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Spinbox(frame_bits, from_=0, to=1, textvariable=self.b1, width=5, command=self.update_inputs).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_bits, text="b2:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tk.Spinbox(frame_bits, from_=0, to=1, textvariable=self.b2, width=5, command=self.update_inputs).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_bits, text="b3:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        tk.Spinbox(frame_bits, from_=0, to=1, textvariable=self.b3, width=5, command=self.update_inputs).grid(row=2, column=1, padx=5, pady=5)
        
        frame_operations = ttk.LabelFrame(self.root, text="Agregar Operación", padding=10)
        frame_operations.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        ttk.Label(frame_operations, text="Operación:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.operation_var = tk.StringVar(value="")
        operations_menu = ttk.Combobox(frame_operations, textvariable=self.operation_var, values=["NOT", "AND", "OR"], state="readonly")
        operations_menu.grid(row=0, column=1, padx=5, pady=5)
        operations_menu.bind("<<ComboboxSelected>>", self.update_operation_inputs)
        
        ttk.Label(frame_operations, text="Input 1:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.input1_var = tk.StringVar(value="")
        self.input1_menu = ttk.Combobox(frame_operations, textvariable=self.input1_var, values=list(self.values.keys()), state="readonly")
        self.input1_menu.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_operations, text="Input 2:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.input2_var = tk.StringVar(value="")
        self.input2_menu = ttk.Combobox(frame_operations, textvariable=self.input2_var, values=list(self.values.keys()), state="readonly")
        self.input2_menu.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(frame_operations, text="Agregar", command=self.add_operation).grid(row=3, column=0, columnspan=2, pady=10)
        
        frame_steps = ttk.LabelFrame(self.root, text="Esquema de Operaciones", padding=10)
        frame_steps.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        self.steps_list = tk.Listbox(frame_steps, height=10, width=40)
        self.steps_list.grid(row=0, column=0, padx=5, pady=5)
        
        ttk.Button(self.root, text="Calcular Resultado", command=self.calculate_result).grid(row=3, column=0, pady=10)
        ttk.Button(self.root, text="Limpiar Esquema", command=self.clear_operations).grid(row=4, column=0, pady=10)
    
    def update_inputs(self):
        self.values["b1"] = self.b1.get()
        self.values["b2"] = self.b2.get()
        self.values["b3"] = self.b3.get()
        self.input1_menu["values"] = list(self.values.keys())
        self.input2_menu["values"] = list(self.values.keys())
    
    def update_operation_inputs(self, event=None):
        operation = self.operation_var.get()
        if operation == "NOT":
            self.input2_menu.set("")
            self.input2_menu["state"] = "disabled"
        else:
            self.input2_menu["state"] = "readonly"
    def add_operation(self):
        operation = self.operation_var.get()
        input1 = self.input1_var.get()
        input2 = self.input2_var.get()
        
        if not operation:
            messagebox.showerror("Error", "Debe seleccionar una operación.")
            return
        
        if operation in ["AND", "OR"]:
            if input1 == input2:
                messagebox.showerror("Error", "Los inputs deben ser diferentes para AND/OR.")
                return
            if not input1 or not input2:
                messagebox.showerror("Error", "Ambos inputs deben estar seleccionados para AND/OR.")
                return
        elif operation == "NOT":
            if not input1:
                messagebox.showerror("Error", "Debe seleccionar un input para NOT.")
                return
        
        result_name = f"R({operation}_{input1},{input2 if operation != 'NOT' else ''},{self.operation_counter})"
        self.operation_counter += 1
        
        self.operations.append((operation, input1, input2, result_name))
        self.steps_list.insert(tk.END, f"{result_name} = {operation}({input1}, {input2 if operation != 'NOT' else ''})")
        
        self.values[result_name] = 0
        self.input1_menu["values"] = list(self.values.keys())
        self.input2_menu["values"] = list(self.values.keys())
    
    def calculate_result(self):
        self.update_inputs()
        
        try:
            for operation, input1, input2, result_name in self.operations:
                if operation == "NOT":
                    result = logica_not(self.values[input1])
                elif operation == "AND":
                    result = logica_and(self.values[input1], self.values[input2])
                elif operation == "OR":
                    result = logica_or(self.values[input1], self.values[input2])
                else:
                    raise ValueError("Operación desconocida.")
                
                self.values[result_name] = result
            
            final_result = list(self.values.values())[-1]
            messagebox.showinfo("Resultado Final", f"El resultado final es: {final_result}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def clear_operations(self):
        self.operations.clear()
        self.steps_list.delete(0, tk.END)
        self.operation_counter = 0
        self.values = {"b1": self.b1.get(), "b2": self.b2.get(), "b3": self.b3.get()}
        self.update_inputs()

root = tk.Tk()
app = LogicSimulatorApp(root)
root.mainloop()