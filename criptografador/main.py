import hashlib
from cryptography.fernet import Fernet

CHAVE = Fernet.generate_key()


class Codificador:
        
    
    def __init__(self) -> None:
        """Classe para critografia de dados
        """
        ...
    
    def md5(self, texto: str) -> str:
        """Método para criptografia usando MD5

        Args:
            texto (str): Texto a ser cripografado

        Returns:
            str: Texto criptografado em MD5 no formado hexadecimal
        """
        hash = hashlib.md5()    
        # Atualiza o objeto hash com a string fornecida em bytes
        hash.update(texto.encode('utf-8'))
        # Retorna a representação hexadecimal do hash MD5
        return hash.hexdigest()    
        
    def criptografia(self, texto: str, chave: bytes):
        """Método responsável pela criptografia de uma string

        Args:
            texto (str): Texto a ser criptografado
            chave (bytes): Objeto com 32 bytes, recomenda-se o uso da
            constante CHAVE presente no código 

        Returns:
            (bytes): Retorna objeto criptografado em bytes
        """
        # Criptografa a string de entrada em bytes
        texto_criptografado = Fernet(chave).encrypt(texto.encode('utf-8'))
        # Retorna o texto criptografado em formato de bytes
        return texto_criptografado
    
    def descriptografia(
        self,
        texto_criptografado: str,
        chave: bytes
        ) -> bytes:
        """Método responsável pela realização da descriptografia
        do método "criptografia" desta classe.
        
        Importante lembrar que para a descriptografia funcione, é 
        preciso usar a mesma chave que foi usado no processo de
        criptografia

        Args:
            texto_criptografado (str):String criptografada
            chave (bytes): Chave usada no processo de criptografia

        Returns:
            bytes: Texto descriptografado
        """
        # Retorna o texto descriptografado 
        return Fernet(chave).decrypt(texto_criptografado)
    

if __name__ == "__main__":
    ...
