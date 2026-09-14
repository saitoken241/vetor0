from pydantic import BaseModel, EmailStr, Field, field_validator


class ContactMessage(BaseModel):
    nome: str = Field(min_length=2, max_length=120)
    email: EmailStr
    empresa: str = Field(default="", max_length=120)
    telefone: str = Field(default="", max_length=40)
    assunto: str = Field(pattern="^(pentest|red-team|conformidade|treinamento|outro)$")
    mensagem: str = Field(min_length=10, max_length=4000)
    consentimento: bool

    @field_validator("consentimento")
    @classmethod
    def consentimento_obrigatorio(cls, v: bool) -> bool:
        if not v:
            raise ValueError("É necessário aceitar o uso dos dados (LGPD).")
        return v
