from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from datetime import datetime
import re

@csrf_exempt
def chat_view(request):
    if request.method != "POST":
        return JsonResponse({"erro": "Método não permitido"}, status=405)

    try:
        data = json.loads(request.body)
        mensagem = data.get("mensagem", "").lower().strip()
    except Exception:
        return JsonResponse({"resposta": "Erro ao processar a mensagem."}, status=400)

    # Normaliza a mensagem: remove acentos e pontuação
    substituicoes = {
        "á": "a", "ã": "a", "â": "a", "à": "a",
        "é": "e", "ê": "e",
        "í": "i",
        "ó": "o", "ô": "o",
        "ú": "u",
        "ç": "c"
    }
    for k, v in substituicoes.items():
        mensagem = mensagem.replace(k, v)

    mensagem = re.sub(r"[^\w\s]", "", mensagem)  # remove pontuação

    # Mapeamento direto
    respostas = {
        "ping": "pong 🏓",
        "status": "Tudo funcionando normalmente ✅",
        "versao": "Versão 1.0.0 do mock",
        "saude": "Servidor saudável e operacional 🩺",
        "health": "OK",
        "oi": "Oi! Tudo bem por aí?",
        "ola": "Olá! Como posso ajudar hoje?",
        "bom dia": "Bom dia, guerreiro! Pronto pra codar?",
        "boa tarde": "Boa tarde! Vamos dominar essa stack!",
        "boa noite": "Boa noite! Vai descansar ou ainda tem deploy pra fazer?",
        "quem te criou": "Fui criado pelo desenvolvedor Alexandre Drummond Rizzato!",
        "como vai": "Tudo certo por aqui! E com você?",
        "do que voce e feito": "Sou um mock esperto feito em Python + Django 💻",
        "por que voce e simples": "Porque até os simples têm poder 😉",
    }

    # Match exato após limpeza
    if mensagem in respostas:
        return JsonResponse({"resposta": respostas[mensagem]})

    # Clima
    if any(p in mensagem for p in ["clima", "tempo", "previsao"]):
        try:
            r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true")
            clima = r.json().get("current_weather", {})
            temp = clima.get("temperature")
            resposta = f"A temperatura atual em São Paulo é de {temp}°C 🌤️"
            return JsonResponse({"resposta": resposta})
        except Exception:
            return JsonResponse({"resposta": "Não consegui obter o clima agora 😢"})

    # Dólar
    if any(p in mensagem for p in ["dolar", "usd", "cotacao"]):
        try:
            r = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
            dolar = r.json()["USDBRL"]
            valor = dolar["bid"]
            resposta = f"A cotação atual do dólar é R$ {valor} 💵"
            return JsonResponse({"resposta": resposta})
        except Exception:
            return JsonResponse({"resposta": "Tive um problema ao buscar a cotação do dólar 😓"})

    # Hora e data
    if any(p in mensagem for p in ["hora", "data", "agora"]):
        agora = datetime.now()
        resposta = agora.strftime("Hoje é %d/%m/%Y e são %H:%M 🕒")
        return JsonResponse({"resposta": resposta})

    # Fallback
    return JsonResponse({"resposta": "Ainda não aprendi a responder isso, mas tô evoluindo! 🚀"})
