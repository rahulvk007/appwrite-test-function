import requests

def main(context):
  if context.req.path == '/eur':
    amount_in_euros = float(context.req.query['amount'])
    response = requests.get('https://api.exchangerate.host/latest?base=EUR&symbols=USD')
    data = response.json()
    amount_in_dollars = amount_in_euros * data['rates']['USD']
    return context.res.send(str(amount_in_dollars))

  if context.req.path == '/inr':
    amount_in_rupees = float(context.req.query['amount'])
    response = requests.get('https://api.exchangerate.host/latest?base=INR&symbols=USD')
    data = response.json()
    amount_in_dollars = amount_in_rupees * data['rates']['USD']
    return context.res.send(str(amount_in_dollars))

  return 'Invalid path'
