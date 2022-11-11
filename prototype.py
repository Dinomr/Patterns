import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):

        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):

        if memo is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)

    # Let's change the list in shallow_copied_component and see if it changes in
    # component.
    shallow_copied_component.some_list_of_objects.append("Otro objeto")
    if component.some_list_of_objects[-1] == "another object":
        print(
            "Añadiendo elementos a `componente copiado de forma superficial "
            "some_list_of_objects añadidos a los `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Añadiendo elementos a `shallow_copied_component`'s "
            "some_list_of_objects no puede ser añadido a `component`'s "
            "some_list_of_objects."
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Cambiando los elementos de `component`'s por algo de _list_of_objects "
            "Cambios en el objeto `shallow_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Cambiando objetos en el `component`'s some_list_of_objects "
            "No realiza el cambio en el objeto `shallow_copied_component`'s "
            "some_list_of_objects."
        )

    deep_copied_component = copy.deepcopy(component)

    # Let's change the list in deep_copied_component and see if it changes in
    # component.
    deep_copied_component.some_list_of_objects.append("Un objeto mas")
    if component.some_list_of_objects[-1] == "Un objeto mas":
        print(
            "Añadiendo elementos a `deep_copied_component`'s "
            "some_list_of_objects añadidos a `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Añadiendo elementos a `deep_copied_component`'s "
            "some_list_of_objects no añadirlo a `component`'s "
            "some_list_of_objects."
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Cambiando los objectos en `component`'s some_list_of_objects "
            "Cambia el objeto en `deep_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Cambiando los objectos en el `component`'s some_list_of_objects "
            "No cambie el objeto en `deep_copied_component`'s "
            "some_list_of_objects."
        )

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ Esto muestra que los objetos copiados en profundidad contienen la misma referencia, ellos "
        "no se clonan repetidamente."
    )