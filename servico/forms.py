# -*- coding: utf-8 -*-
from django import forms

from cadastro.models import Usuario
from .models import *

class FormEquipamento(forms.ModelForm):
	class Meta:
		model = Equipamento

		fields = ['codigo', 'nome', 'descricao']

class FormServico(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super (FormServico,self ).__init__(*args,**kwargs) # populates the post
		self.fields['funcionario'].queryset = Usuario.objects.filter(tipo=3)
	
	class Meta:
		model = Servico
 
		fields = ['tipo', 'codigo', 'data_de_inicio', 'data_de_fim', 'descricao', 
		'valor', 'status', 'situacao', 'funcionario', 'cliente', 'equipamento',]
		
		widgets = {
			'data_de_inicio': forms.SelectDateWidget,
			'data_de_fim': forms.SelectDateWidget,
			'funcionario' : forms.CheckboxSelectMultiple(),
		}			