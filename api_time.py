import requests
import configs as cfg

url = f'https://api.openweathermap.org/data/2.5/weather?q={cfg.CITY_NAME}&appid={cfg.API_KEY}&lang={cfg.LANG}'
requisicao = requests.get(url)

def verify_atributos():
    """
        Método que vai verificar se a requisição deu certo
    """

    if str(requisicao) == "<Response [200]>":
        return exibir_request()
    else:
        raise ValueError("Erro na conexão")
    
def exibir_request():

    requests_dict = requisicao.json()
    
    len_city = "Cidade : " + cfg.CITY_NAME
    description = "Descrição : " + str(requests_dict['weather'][0]['description'])
    temp = "Temperatura : {:.2f} °C".format(requests_dict['main']['temp'] - 273.15)
    temp_max = "Temperatura máxima : {:.2f} °C".format(requests_dict['main']['temp_max'] - 273.15)
    temp_min = "Temperatura mínima : {:.2f} °C".format(requests_dict['main']['temp_min'] - 273.15)

    return len_city + "\n" + description + "\n" + temp + "\n" + temp_max + "\n" + temp_min

if __name__ == "__main__":
    print("Este é o código que será executado apenas quando o arquivo main for executado.")