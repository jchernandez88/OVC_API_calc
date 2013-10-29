# -*- coding: utf-8 -*- 
from django.db import models

class Operacion(models.Model):
    OPERACIONES = (
        (u'+', u'Suma'),
        (u'-', u'Resta'),
        (u'*', u'Multiplicación'),
        (u'/', u'División'),
    )
    op1 = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        default=0.0,
        help_text='Operador 1',
        )
    op2 = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        default=0.0,
        help_text='Operador 2',
        )
    operacion = models.CharField(
        max_length=1,
        choices=OPERACIONES,
        default='+',
        help_text='Seleccione una operación',
        )
    resultado = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        null=True,
        blank=True,
        help_text='El resultado de la operación',
        )

    def __unicode__(self):
        return "%s %s %s = %s" % (self.op1,self.operacion,self.op2,self.resultado)

    def save(self, **kwargs):
        res = 0.0
        if self.operacion == '*':
            res = self.op1 * self.op2
        elif self.operacion == '/':
            if self.op2 != 0:
                res = self.op1 / self.op2
        elif self.operacion == '-':
            res = self.op1 - self.op2
        else:
            res = self.op1 + self.op2
        self.resultado = res
        super (Operacion, self).save()

