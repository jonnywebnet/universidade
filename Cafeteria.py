class ItemPedido:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade

    def __str__(self):
        return f"{self.quantidade}x {self.nome} - Subtotal: R${self.subtotal():.2f}"

class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.status = "pendente"
        self.itens = []        # nasce aqui

    def adicionar_item(self, item):
        self.itens.append(item)

    def total(self):
        return sum(item.subtotal() for item in self.itens)

    def __str__(self):
        return f"pedido {self.numero} | Cliente: {self.cliente} | Status: {self.status} | Total: R${self.total():.2f}"

class Cafeteria:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []        # nasce aqui

    def registrar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        for pedido in self:
            for pedido in self.pedidos:
                print(pedido)

    def buscar_por_cliente(self, trecho):
        return [pedido for pedido in self.pedidos if trecho.lower() in pedido.cliente.lower()]

    def itens_do_pedido(self, numero):
        for pedido in self.pedidos:
            if pedido.numero == numero:
                return pedido.itens
        return []
 
class Cozinha:
    def __init__(self, responsavel):
        self.responsavel = responsavel
        
    def preparar(self, pedido):
        for item in pedido.itens:
            print(item.nome)
        pedido.status = "pronto"

if __name__ == "__main__":
    p1 = Pedido(1, "Zé da manga")
    p2 = Pedido(2, "Mariazinha")
    p3 = Pedido(3, "Professor Diego")

    p1.adicionar_item(ItemPedido("Café", 5.0, 2))
    p1.adicionar_item(ItemPedido("Bolo", 3.0, 1))

    p2.adicionar_item(ItemPedido("Chá", 5.0, 2))
    p2.adicionar_item(ItemPedido("Pão", 3.0, 1))

    p3.adicionar_item(ItemPedido("Suco", 5.0, 2))
    p3.adicionar_item(ItemPedido("Torta", 3.0, 1))

    cafe = Cafeteria("Café Aurora")
    cafe.registrar_pedido(p1)
    cafe.registrar_pedido(p2)
    cafe.registrar_pedido(p3)

    for pedido in cafe.pedidos:
        print(f"Cliente: {pedido.cliente} | Total: R${pedido.total():.2f}")
        for item in pedido.itens:
            print(f"  -{item.nome}")

    cozinha = Cozinha("Chef João")
    print(f"\nStatus antes {p1.status}")
    cozinha.preparar(p1)
    print(f"Status depois: {p1.status}" )

    pedido_removido = cafe.pedidos.pop(0)
    print(f"\nPedido removido: {pedido_removido}")
