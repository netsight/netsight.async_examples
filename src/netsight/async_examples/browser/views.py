import locale

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import transaction

from netsight.async.browser.BaseAsyncView import BaseAsyncView


class AsyncExample1(BaseAsyncView):
    def __run__(self, process_id=None, *args, **kwargs):
        self.set_progress(process_id, 0)
        
        number = 0
        try:
            number = int(self.request.get('number')) - 1
        except (TypeError, ValueError), e:
            pass
        
        f = [0, 1]
        count = 1
        while count <= number:
            f.append(f.pop(0) + f[0])
            self.set_progress(process_id, count/float(number) * 100.0)
            count += 1
            transaction.commit()
            
        result = locale.format('%d', f[1], grouping=True)
                
        return ViewPageTemplateFile('templates/async_result_1.pt')(self, result=result)
