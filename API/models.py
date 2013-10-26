from django.db import models

class Operacion(models.Model):
    OPERACIONES = (
        (u'+', u'Suma'),
        (u'-', u'Resta'),
        (u'*', u'Multiplicacion'),
        (u'/', u'Division'),
    )
    op1 = models.DecimalField(max_digits=14,decimal_places=4)
    op2 = models.DecimalField(max_digits=14,decimal_places=4)
    operacion = models.CharField(max_length=1, choices=OPERACIONES)
    resultado = models.DecimalField(max_digits=14,decimal_places=4)

    def __unicode__(self):
        return "%s %s %s = %s" % (self.op1,self.operacion,self.op2,self.resultado)
