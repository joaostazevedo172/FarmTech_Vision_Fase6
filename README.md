# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="https://tse2.mm.bing.net/th/id/OIP.3xs_MSeNC0T1UOrJaCEqWAHaEK?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br># 🐄 FarmTech Solutions - Sistema de Visão Computacional (Fase 6)

Este repositório contém o desenvolvimento de um sistema de inteligência artificial voltado para a **saúde animal e segurança patrimonial**, desenvolvido para a FarmTech Solutions. O projeto compara abordagens de detecção de objetos (YOLOv5) e classificação de imagens (CNN Customizada).

---

## 📺 Demonstração em Vídeo
Confira a explicação detalhada do projeto, a execução do código e a análise dos resultados no link abaixo:
👉 **https://www.youtube.com/watch?v=yF7pLSVUty4** 

## 📺 GitHub
Confira o link do GitHub
👉 **https://github.com/joaostazevedo172/FarmTech_Vision_Fase6** 


## 👨‍🌾 Integrantes do Grupo
- <a href="#">Miriã Leal Mantovani</a>
- <a href="#">João Pedro Santos Azevedo</a> 
- <a href="#">Rodrigo de Souza Freitas</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://github.com/SabrinaOtoni">Sabrina Otoni</a>

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Frameworks:** PyTorch (YOLOv5), TensorFlow/Keras (CNN)
* **Ferramentas:** Google Colab, Make Sense AI (Rotulação), GitHub.
* **Dataset:** 80 imagens de cachorros e gatos (Treino, Validação e Teste).

---

## 📂 Estrutura do Repositorio
* `notebooks/`: Contém o arquivo `.ipynb` principal com todo o código executado.
* `weights/`: O arquivo `best.pt` contendo os pesos treinados da YOLOv5 (60 épocas).
* `README.md`: Documentação do projeto.

---

## 📊 Comparativo de Modelos

Para a FarmTech Solutions, avaliamos três abordagens distintas para garantir a melhor entrega ao cliente:

| Critério | YOLOv5 Custom (60 ep) | CNN (Do Zero) | YOLO Padrão |
| :--- | :--- | :--- | :--- |
| **Precisão (mAP/Acc)** | **~90%** | **~75%** | Baixa |
| **Tempo de Treino** | 7-8 min | 2-3 min | N/A |
| **Localização** | Sim (Bounding Box) | Não (Apenas Classe) | Sim |

---

## 📈 Conclusões Críticas
1. **YOLOv5 Customizada:** Foi o modelo de maior sucesso. Graças ao *Transfer Learning*, ele conseguiu identificar animais com alta confiança mesmo com um dataset pequeno de 80 imagens.
2. **CNN do Zero:** Demonstrou ser uma alternativa leve, porém menos precisa para localização espacial, sendo recomendada apenas para triagem rápida de imagens.
3. **Escalabilidade:** Para o ambiente de fazendas da FarmTech, a detecção em tempo real da YOLOv5 é a solução ideal para monitoramento de segurança.

---

## 🚀 Como Rodar o Projeto
1. Clone este repositório.
2. Faça o upload do arquivo `.ipynb` para o [Google Colab](https://colab.research.google.com/).
3. Certifique-se de que o seu Google Drive contenha a pasta `dataset_visao_computacional` conforme a estrutura exigida no notebook.
4. Execute as células em ordem para reproduzir os treinos e testes.

---

