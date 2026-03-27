import cv2
import torch
import pathlib

# --- A MÁGICA PARA O WINDOWS LER O ARQUIVO DO LINUX ---
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
# ------------------------------------------------------

print("Iniciando o sistema de segurança da FarmTech Solutions...")
print("Carregando o modelo customizado (isso pode levar alguns segundos)...")

# 1. Carregar o modelo YOLOv5
# (O caminho está configurado para a sua estrutura de pastas!)
modelo = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/weight_60_epocas/best.pt', force_reload=True)

# Ajuste de confiança (só mostra se tiver 40% ou mais de certeza)
modelo.conf = 0.40 

# 2. Iniciar a captura de vídeo (0 é a webcam padrão do PC)
cap = cv2.VideoCapture(0)

print("Câmera ativada! Pressione a tecla 'q' na janela do vídeo para fechar.")

while True:
    # Ler o frame da câmera
    sucesso, frame = cap.read()
    if not sucesso:
        print("Erro ao acessar a câmera.")
        break

    # 3. Fazer a detecção no frame atual
    resultados = modelo(frame)

    # 4. Renderizar as caixas de detecção no frame
    frame_processado = resultados.render()[0]

    # Mostrar o vídeo na tela
    cv2.imshow('Visao Computacional - FarmTech Solutions', frame_processado)

    # 5. Condição de parada (apertar a tecla 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Desligar a câmera e fechar as janelas
cap.release()
cv2.destroyAllWindows()