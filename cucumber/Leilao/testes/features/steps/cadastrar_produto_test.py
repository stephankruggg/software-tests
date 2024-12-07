from behave import *
from src.mercado_leilao import MercadoLeilao

@given('o cadastro do usuario {nome_usuario} foi realizado')
def step_impl(context, nome_usuario):
    context.mercado = MercadoLeilao()
    context.mercado.cadastra_usuario(
        nome_usuario,
        'Campus Universitario',
        'ernani.santos@posgrad.ufsc.br',
        '055.761.919-00'
    )

@given('o nome do produto {nome_produto}')
def step_impl(context, nome_produto):
    context.nome_produto = nome_produto

@given('{nome_produto} {descricao_produto} ja foi cadastrado')
def step_impl(context, nome_produto, descricao_produto):
    context.mercado.cadastra_produto(
            nome_produto,
            descricao_produto,
            100,
            '055.761.919-00',
            '1'
        )

@given('a descricao do produto {descricao_produto}')
def step_impl(context, descricao_produto):
    context.descricao_produto = descricao_produto

@given('e o lance {lance}')
def step_impl(context, lance):
    context.lance = lance

@given('e o cpf do leiloador {cpf_leiloador}')
def step_impl(context, cpf_leiloador):
    context.cpf_leiloador = cpf_leiloador

@when('cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(
            context.nome_produto,
            context.descricao_produto,
            context.lance,
            context.cpf_leiloador,
            '1'
        )
    except Exception as e:
        context.msg = e.__str__()

@then('o sistema cadastra com sucesso')
def step_impl(context):
    assert context.mercado.existe_produto(context.nome_produto) == True

@then('o sistema mostra a mensagem {mensagem}')
def step_impl(context, mensagem):
    assert mensagem == context.msg
