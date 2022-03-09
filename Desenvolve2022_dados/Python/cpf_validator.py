from validate_docbr import CPF, CNPJ


class CpfCnpj:
    def __init__(self, documento, tipo_do_documento):
        self.tipo_do_documento = tipo_do_documento
        documento = str(documento)
        if tipo_do_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError ("CPF Inválido.")
        elif tipo_do_documento == "cnpj":
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido")
        else:
            raise ValueError("Documento inválido")

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
         return self.format_cpf()

    def cnpj_eh_valido(self, cnpj):
         if len(cnpj) == 14:
            validade_cnpj = CNPJ()
            return validade_cnpj.validate(cnpj)
         else:
            raise ValueError("Quantidade de dígitos inválidos!")

    def __len__(self):
        return len(self)

cpf_um = CpfCnpj(15316264754, 'cpf')

cpf_um.cpf_eh_valido(cpf_um)



