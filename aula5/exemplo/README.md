# Ollama

Para acessar um arquivo `modelfile` e ter o exemplo de criação:

```shell
ollama show llama2  --modelfile
```

## Criação de um arquivo modelo

Para criar um arquivo `modelfile` com base em um existente, baste executar o seguinte comando:

```shell
ollama show {seu modelo} --modelfile > new.modelfile
```

Ex.:

```shell
ollama show llama --modelfile > new.modelfile
```

A seguir temos um exemplo de customização:

```shell
FROM llama2:latest
TEMPLATE """{{ if .System }}System: {{ .System }}{{ end }}
User: {{ .Prompt }}
Assistant:"""
SYSTEM """Este é um chat entre um usuário e um assistente de inteligência artificial especializado em investimentos no Brasil, que oferece orientações sobre temas como renda fixa, renda variável, fundos de investimento e estratégias financeiras. O assistente responde de maneira clara e personalizada, ajudando o usuário a entender melhor as opções de investimento e a tomar decisões informadas com base em seu perfil e objetivos."""
PARAMETER stop "User:"
PARAMETER stop "Assistant:"
PARAMETER stop "System:"
```

## Criacao do modelo

Para criar o modelo você pode utilizar o seguinte comando:

```shell
ollama create {nome do modelo} --file new.modelfile
```

Ex.:

```shell
ollama create fiap-model-finance --file new.modelfile
```