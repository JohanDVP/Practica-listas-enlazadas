import random

class NodeD:

    __slots__ = ("__value","__next","__prev")

    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None

    def __str__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @value.setter
    def value(self, new_value):
        if new_value is None:
            raise TypeError("El nodo no puede contener valores nulos")
        self.__value = new_value

    @next.setter
    def next(self, new_next):
        if new_next is not None and not isinstance(new_next,NodeD):
            raise TypeError("El next de un nodo, solo puede ser None ó un objeto tipo nodo")
        self.__next = new_next

    @prev.setter
    def prev(self, new_prev):
        if new_prev is not None and not isinstance(new_prev,NodeD):
            raise TypeError("El next de un nodo, solo puede ser None ó un objeto tipo nodo")
        self.__prev = new_prev




class dlinkedlist:

    __slots__ = ("__head","__tail","__size")

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0


    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def size(self):
        return self.__size

    @head.setter
    def head(self, new_head):
        if new_head is not None and not isinstance(new_head,NodeD):
            raise TypeError("La cabeza de una lista enlazada, solo puede ser None ó un objeto tipo nodo")
        self.__head = new_head

    @tail.setter
    def tail(self, new_tail):
        if new_tail is not None and not isinstance(new_tail,NodeD):
            raise TypeError("La cola de una lista enlazada, solo puede ser None ó un objeto tipo nodo")
        self.__tail = new_tail

    @size.setter
    def size(self, new_size):
        if new_size < 0 and not isinstance(new_size,int):
            raise TypeError("El tamaño de una lista enlazada, solo puede ser un numero entero mayor ó igual a cero")
        self.__size = new_size

    def __iter__(self):
        cur_node = self.__head

        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def __str__(self):
        result = [str(temp_node.value) for temp_node in self]
        return ' <--> '.join(result)


    def prepend(self, new_value):
        new_node = NodeD(new_value)

        new_node.next = self.__head
        if self.__head is None:
            self.__tail = new_node
        else:
            self.__head.prev = new_node

        self.__head = new_node
        self.__size += 1

    def append(self, new_value):
        new_node = NodeD(new_value)

        if self.__head is None:
            self.__head = new_node
        else:
            self.__tail.next = new_node

        new_node.prev = self.__tail
        self.__tail = new_node
        self.__size += 1

    def getbyIndex(self, index):

        if not isinstance(index,int) or index > self.__size -1 or index < -1:
            raise TypeError("el parametro indice esta por fuera de rango ó es un valor del tipo incorrecto")

        if index == 0:
            return self.head.value
        elif index == -1 or index == self.__size -1:
            return self.__tail.value
        else:
            index_temp = 0

            for cur_node in self:
                if index_temp == index:
                    return cur_node.value
                index_temp += 1


    def getNodebyIndex(self, index):

        if not isinstance(index,int) or index > self.__size -1 or index < -1:
            raise TypeError("el parametro indice esta por fuera de rango ó es un valor del tipo incorrecto")

        if index == 0:
            return self.head
        elif index == -1 or index == self.__size -1:
            return self.__tail
        else:
            index_temp = 0

            for cur_node in self:
                if index_temp == index:
                    return cur_node
                index_temp += 1


    def InsertbyIndex(self, index, new_value):

        if not isinstance(index,int) or index > self.__size or index < -1:
            raise TypeError("el parametro indice esta por fuera de rango ó es un valor del tipo incorrecto")


        if index == 0:
            self.prepend(new_value)
        elif index == -1 or index == self.__size:
            self.append(new_value)
        else:
            new_node = NodeD(new_value)
            prev_node = self.getNodebyIndex(index-1)
            next_node = prev_node.next
            print("prev_node", prev_node)
            print("new_node", new_node)
            print("next_node",next_node)

            print("new_node.next antes", new_node.next)
            new_node.next = next_node
            print("new_node.next despues", new_node.next)
            print("prev_node.next antes", prev_node.next)
            prev_node.next = new_node
            print("prev_node.next despues", prev_node.next)
            new_node.prev = prev_node
            print("new_node.prev despues", new_node.prev)
            print("next_node.prev antes", next_node.prev)
            next_node.prev = new_node
            print("next_node.prev despues", next_node.prev)

            self.__size += 1


    def searchvalue(self, value_to_find):
        for cur_node in self:
          if value_to_find == cur_node.value:
            return True

        return False

    def set_newvalue(self, value, new_value):
        for cur_node in self:
          if value == cur_node.value:
            cur_node.value = new_value

        return False

    def popfirst(self):
        if self.__head is None:
            raise TypeError("No hay elementos para retornar")
        elif self.__head is self.__tail:
            temp_value = self.__head.value
            self.__head = None
            self.__tail = None
            self.__size = 0
        else:
            temp_value = self.__head.value
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size -= 1

        return temp_value


    def pop(self):
        if self.__head is None:
            raise TypeError("No hay elementos para retornar")
        elif self.__head is self.__tail:
            temp_value = self.__head.value
            self.__head = None
            self.__tail = None
            self.__size = 0
        else:
            temp_value = self.__tail.value
            prev_tail = self.__tail.prev
            print("prev_tail :", prev_tail)
            prev_tail.next = None

            self.__tail = prev_tail
            self.__size -= 1


        return temp_value

    def generate(self, n, minvalue, maxvalue):
        for i in range(n):
            self.append(random.randint(minvalue, maxvalue))
        return self


    def swap_nodes(self):

        new_head = self.head.next
        cur_node = self.head
        prev_node = NodeD("")

        while cur_node and cur_node.next:
            print("cur_node",cur_node)
            next_node = cur_node.next
            print("next_node", next_node)
            print("prev_node", prev_node)

            cur_node.next = next_node.next
            print("cur_node.next despues", cur_node.next)
            cur_node.prev = next_node
            print("cur_node.prev despues", cur_node.prev)

            #cambiemos apuntadores del next
            next_node.prev = prev_node
            print("next_node.prev despues", next_node.prev)
            next_node.next = cur_node
            print("next_node.next despues", next_node.next)

            prev_node.next = next_node
            print("prev_node.next despues", prev_node.next)

            prev_node = cur_node
            cur_node = cur_node.next


        self.head = new_head
        self.head.prev = None

    def registrar_paciente(self, id_paciente, categoria, nivel_triage):
        Npaciente = Paciente(id_paciente, categoria, nivel_triage)
        self.append(Npaciente)

    def atencion_prioritaria_inmediata(self):
        if self.head is None:
            return

        current_node = self.tail

        for i in range(self.size):
            nodo_previo = current_node.prev

            if current_node.value.categoria == "tercera_edad" and current_node.value.nivel_triage == 1:
                
                if current_node is not self.head:
                    
                    if current_node.next is None:
                        current_node.prev.next = None
                        self.tail = current_node.prev

                    else:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev

                    antigua_cabeza = self.head
                    self.head = current_node
                    self.head.next = antigua_cabeza
                    antigua_cabeza.prev = self.head
                    self.head.prev = None

            current_node = nodo_previo

    def depuracion_de_consulta_externa(self):
        if self.head is None:
            return
        
        current_node = self.head

        for i in range(self.size):

            nodo_siguiente = current_node.next

            if current_node.value.categoria == "adulto" and current_node.value.nivel_triage > 3:

                if current_node.prev is None and current_node.next is None:
                    self.head = None
                    self.tail = None

                elif current_node.prev is None:
                    self.head = current_node.next
                    self.head.prev = None

                elif current_node.next is None:
                    current_node.prev.next = None
                    self.tail = current_node.prev

                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev

                current_node.next = None
                current_node.prev = None
                self.size -= 1

            current_node = nodo_siguiente

    def aislamiento_por_zona_de_contagio(self, id_inicio, id_final):
        lista_aislamiento = dlinkedlist()

        if self.head is None:
            return lista_aislamiento

        pos_inicio = None
        pos_final = None
        id = 0

        for nodo_actual in self:
            if nodo_actual.value.id_paciente == id_inicio:
                pos_inicio = id
            if nodo_actual.value.id_paciente == id_final:
                pos_final = id
            id += 1

        if pos_inicio is None or pos_final is None:
            return lista_aislamiento

        if pos_inicio > pos_final:
            temp = pos_inicio
            pos_inicio = pos_final
            pos_final = temp

        if pos_final - pos_inicio <= 1:
            return lista_aislamiento
    
        current_node = self.head
        index = 0

        while (pos_inicio + 1) != index:
            current_node = current_node.next
            index += 1

        inicio_bloque = current_node

        while (pos_final - 1) != index:
            current_node = current_node.next
            index += 1

        fin_bloque = current_node

        nodo_antes = inicio_bloque.prev
        nodo_despues = fin_bloque.next

        nodo_antes.next = nodo_despues
        nodo_despues.prev = nodo_antes

        inicio_bloque.prev = None
        fin_bloque.next = None

        lista_aislamiento.head = inicio_bloque
        lista_aislamiento.tail = fin_bloque

        self.size -= (pos_final - pos_inicio) - 1
        lista_aislamiento.size = (pos_final - pos_inicio) - 1

        return lista_aislamiento

    def inversion_condicional_de_flujo(self):
        if self.head is None:
            return

        cantidad_cat_pediatria = 0
        cantidad_cat_adulto = 0
        
        for current in self:
            if current.value.categoria == "pediatria":
                cantidad_cat_pediatria += 1
            elif current.value.categoria == "adulto":
                cantidad_cat_adulto += 1

        if cantidad_cat_pediatria > cantidad_cat_adulto:
            current_node = self.head

            for i in range(self.size):
                siguiente_nodo = current_node.next

                temporal = current_node.next
                current_node.next = current_node.prev
                current_node.prev = temporal

                current_node = siguiente_nodo

            antigua_cabeza = self.head
            self.head = self.tail
            self.tail = antigua_cabeza

    def reorganización_multicriterio_estable(self):
        if self.head is None:
            return

        current_node = self.head.next

        while current_node is not None:

            siguiente_nodo = current_node.next
            nodo_anterior = current_node.prev

            while nodo_anterior is not None:

                va_antes = False

                if current_node.value.nivel_triage < nodo_anterior.value.nivel_triage:
                    va_antes = True

                elif current_node.value.nivel_triage == nodo_anterior.value.nivel_triage:

                    prioridad_actual = 0
                    prioridad_anterior = 0

                    if current_node.value.categoria == "tercera_edad":
                        prioridad_actual = 1
                    elif current_node.value.categoria == "pediatria":
                        prioridad_actual = 2
                    else:
                        prioridad_actual = 3

                    if nodo_anterior.value.categoria == "tercera_edad":
                        prioridad_anterior = 1
                    elif nodo_anterior.value.categoria == "pediatria":
                        prioridad_anterior = 2
                    else:
                        prioridad_anterior = 3

                    if prioridad_actual < prioridad_anterior:
                        va_antes = True

                if va_antes:
                    nodo_anterior = nodo_anterior.prev
                else:
                    break

            if nodo_anterior is not current_node.prev:

                if current_node.next:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    current_node.prev.next = None
                    self.tail = current_node.prev

                if nodo_anterior is None:

                    current_node.prev = None
                    current_node.next = self.head
                    self.head.prev = current_node
                    self.head = current_node

                else:

                    siguiente = nodo_anterior.next

                    current_node.prev = nodo_anterior
                    current_node.next = siguiente

                    nodo_anterior.next = current_node

                    if siguiente:
                        siguiente.prev = current_node
                    else:
                        self.tail = current_node

            current_node = siguiente_nodo

    def intercalado_de_emergencia(self, lista_derivados):
        if lista_derivados.head is None:
            return
        
        if self.head is None:
            self.head = lista_derivados.head
            self.tail = lista_derivados.tail

            self.size = lista_derivados.size
            lista_derivados.size = 0

            lista_derivados.head = None
            lista_derivados.tail = None
            return

        actual_principal = self.head
        actual_derivado = lista_derivados.head
        contador = 0

        while actual_principal is not None and actual_derivado is not None:

            contador += 1

            if contador == 2:

                siguiente_derivado = actual_derivado.next
                siguiente_principal = actual_principal.next

                if actual_derivado.prev:
                    actual_derivado.prev.next = actual_derivado.next
                else:
                    lista_derivados.head = actual_derivado.next

                if actual_derivado.next:
                    actual_derivado.next.prev = actual_derivado.prev
                else:
                    lista_derivados.tail = actual_derivado.prev

                actual_derivado.prev = actual_principal
                actual_derivado.next = siguiente_principal
                actual_principal.next = actual_derivado

                if siguiente_principal:
                    siguiente_principal.prev = actual_derivado
                else:
                    self.tail = actual_derivado

                contador = 0
                actual_derivado = siguiente_derivado
                actual_principal = siguiente_principal

            else:
                actual_principal = actual_principal.next

        if actual_derivado is not None:
            resto_head = actual_derivado
            resto_tail = lista_derivados.tail

            self.tail.next = resto_head
            resto_head.prev = self.tail
            self.tail = resto_tail

        self.size += lista_derivados.size

        lista_derivados.head = None
        lista_derivados.tail = None
        lista_derivados.size = 0

class Paciente:
    def __init__(self, id_paciente, categoria, nivel_triage):
      self.id_paciente = id_paciente
      self.categoria = categoria
      self.nivel_triage = nivel_triage

    def __str__(self):
        return f"{self.id_paciente}({self.categoria},t{self.nivel_triage})"

