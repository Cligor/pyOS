PAGE_SIZE_BITS = 6
PAGE_SIZE = (1 << PAGE_SIZE_BITS)
MEMORY_SIZE_WITH_OS = (16*1024)
MEMORY_SIZE_WITHOUT_OS = 256

# registradores
NREGS = 8

# falha de proteção de memória
INTERRUPT_MEMORY_PROTECTION_FAULT       = 1

# teclado
INTERRUPT_KEYBOARD                      = 2

# temporizador
INTERRUPT_TIMER                         = 3


# ciclos para interrupção do processador
TIMER_THRESHOLD = 200