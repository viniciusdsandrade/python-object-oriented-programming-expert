# 6. Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve conseguir informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas
# válidas.

class TV:
    def __init__(self, canal: int, volume: float = 0.0):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, canal):
        if 0 <= canal <= 100:
            self.canal = canal
        else:
            print('Canal inválido')

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print('Volume máximo')

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print('Volume mínimo')

    def __str__(self):
        return f'Canal: {self.canal} - Volume: {self.volume}'
