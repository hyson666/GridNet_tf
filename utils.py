import sys

def show_progress(epoch, batch, batch_total, loss, acc):
    sys.stdout.write(f'\r{epoch} epoch: [{batch}/{batch_total}, loss: {loss}, acc: {acc}]')
    sys.stdout.flush()
