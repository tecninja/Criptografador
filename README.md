# Criptografador
Proposta de pacote para abstração de criptografia e descriptografia.

Forma de uso:</br>

Criptografia com uso de chave</br>

<code>
>>>from criptografador import Codificador, CHAVE </br>
>>>texto = "Olá mundo" </br>
>>>texto_criptografado = Codificador().criptografia(texto, CHAVE)</br>
>>>print(texto_criptografado)</br>
b'gAAAAABkyrflX7sM6Fg9kdCxfhMN4bFheFu8oqM5lK5MUxbGa9WmxwcybhsW7cUvOdr4zZNgyzRuurNQviJtR1XV_F13vvLshw=='</br></br>
</code>

Descriptografia com uso de chave</br>

<code>
>>>texto_descriptografado = Codificador().descriptografia(texto_criptografado, CHAVE).decode()</br>
>>>print(texto_descriptografado)</br>
Olá mundo</br></br>
</code>


Criptografia em MD5</br>

<code>
>>>texto_md5 = Codificador().md5(texto)</br>
>>>print(texto_md5)</br>
622573cfe5b2ea9a8ce8cc5570bb0407</br>
</code>

