from ultralytics import YOLO

# Carrega o modelo treinado (ajuste o caminho para o arquivo .pt gerado)
model = YOLO('runs/detect/train/weights/best.pt')

# Executa a inferência numa imagem
results = model('images/val/ross48.png')

# Mostra a imagem com as detecções (acessando o primeiro item da lista)
results[0].show()
