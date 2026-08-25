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
        if self.head is None:
            return lista_aislamiento
        
        lista_aislamiento = dlinkedlist()

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
            pos_inicio, pos_final = pos_final, pos_inicio

        if pos_final - pos_inicio <= 1:
            return lista_aislamiento
    
        current_node = self.head
        index = 0

        while (pos_inicio + 1) != index:
            current_node = current_node.next
            index += 1

        for i in range((pos_final - pos_inicio) - 1):
            siguiente_nodo = current_node.next

            if current_node.prev is None:
                self.head = current_node.next
                self.head.prev = None
                
            elif current_node.next is None:
                current_node.prev.next = None
                self.tail = current_node.prev
                
            else:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

            if lista_aislamiento.head is None:
                lista_aislamiento.head = current_node
                lista_aislamiento.tail = current_node

            else:
                lista_aislamiento.tail.next = current_node
                current_node.prev = lista_aislamiento.tail
                lista_aislamiento.tail = current_node

            self.size -= 1
            lista_aislamiento.size += 1
            current_node = siguiente_nodo

        return lista_aislamiento


            
            






            
class Paciente:
    def __init__(self, id_paciente, categoria, nivel_triage):
      self.id_paciente = id_paciente
      self.categoria = categoria
      self.nivel_triage = nivel_triage

