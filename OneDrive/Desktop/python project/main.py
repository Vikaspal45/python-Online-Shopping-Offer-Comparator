def get_sample_offers():
    return [
        {'store': 'Amazon', 'original_price': 2999, 'discount_percent': 20, 
         'coupon_discount': 10, 'delivery_fee': 0, 'tax_percent': 12, 
         'quantity': 1, 'delivery_days': 2},
        {'store': 'Flipkart', 'original_price': 2999, 'discount_percent': 25,
         'coupon_discount': 25, 'delivery_fee': 50, 'tax_percent': 12,
         'quantity': 1, 'delivery_days': 3},
        {'store': 'Myntra', 'original_price': 2999, 'discount_percent': 15,
         'coupon_discount': 0, 'delivery_fee': 30, 'tax_percent': 12,
         'quantity': 1, 'delivery_days': 5},
        {'store': 'Snapdeal', 'original_price': 2999, 'discount_percent': 30,
         'coupon_discount': 0, 'delivery_fee': 75, 'tax_percent': 12,
         'quantity': 1, 'delivery_days': 4}
    ]

def get_user_offers():
    offers = []
    print("\n📝 Enter your own offers:")
    print("   (Type 'done' as store name to finish)\n")
    
    while True:
        store = input("Store name (or 'done'): ").strip()
        if store.lower() == 'done':
            break
        
        try:
            original = float(input("Original price (₹): "))
            discount = float(input("Discount percentage: "))
            if discount > 100:
                print("❌ Discount cannot exceed 100%!")
                continue
            coupon = float(input("Coupon discount (₹, 0 if none): "))
            delivery = float(input("Delivery fee (₹): "))
            tax = float(input("Tax percentage: "))
            if tax < 0:
                print("❌ Tax cannot be negative!")
                continue
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("❌ Quantity must be at least 1!")
                continue
            days = int(input("Delivery days: "))
            if days <= 0:
                print("❌ Delivery days must be positive!")
                continue
            
            offer = {
                'store': store,
                'original_price': original,
                'discount_percent': discount,
                'coupon_discount': coupon,
                'delivery_fee': delivery,
                'tax_percent': tax,
                'quantity': quantity,
                'delivery_days': days
            }
            offers.append(offer)
            print(f"✅ Added {store}\n")
            
        except ValueError:
            print("❌ Invalid input! Please enter numbers correctly.\n")
    
    return offers

def calculate_final_price(offer):
    original = offer['original_price']
    discount_amount = (original * offer['discount_percent']) / 100
    after_discount = original - discount_amount
    after_coupon = after_discount - offer['coupon_discount']
    if after_coupon < 0:
        after_coupon = 0
    tax_amount = (after_coupon * offer['tax_percent']) / 100
    after_tax = after_coupon + tax_amount
    final_price = after_tax + offer['delivery_fee']
    total_price = final_price * offer['quantity']
    total_savings = (original - after_discount) * offer['quantity']
    
    return {
        'total_price': total_price,
        'total_savings': total_savings,
        'original_price': original,
        'discount_amount': discount_amount,
        'after_discount': after_discount,
        'coupon_discount': offer['coupon_discount'],
        'after_coupon': after_coupon,
        'tax_amount': tax_amount,
        'after_tax': after_tax,
        'delivery_fee': offer['delivery_fee'],
        'final_price': final_price,
        'quantity': offer['quantity']
    }

def compare_offers(offers):
    results = []
    for offer in offers:
        calc = calculate_final_price(offer)
        results.append({
            'store': offer['store'],
            'final_price': calc['total_price'],
            'savings': calc['total_savings'],
            'delivery_days': offer['delivery_days'],
            'calculation': calc,
            'offer': offer
        })
    results.sort(key=lambda x: x['final_price'])
    return results

def display_results(results):
    if not results:
        print("No offers to compare!")
        return
    
    print("\n" + "="*70)
    print("     🛍️  SHOPPING OFFER COMPARISON REPORT")
    print("="*70)
    
    print(f"\n{'Store':<15} {'Final Price':<15} {'Savings':<15} {'Delivery'}")
    print("-"*70)
    
    for i, result in enumerate(results):
        best = "💰 BEST" if i == 0 else ""
        print(f"{result['store']:<15} ₹{result['final_price']:<14.2f} "
              f"₹{result['savings']:<14.2f} {result['delivery_days']} days   {best}")
    
    print("-"*70)
    
    print("\n🎯 RECOMMENDATIONS:")
    print("-"*70)
    print(f"💰 Cheapest: {results[0]['store']} at ₹{results[0]['final_price']:.2f}")
    
    fastest = min(results, key=lambda x: x['delivery_days'])
    print(f"🚀 Fastest delivery: {fastest['store']} - {fastest['delivery_days']} days")
    
    most_savings = max(results, key=lambda x: x['savings'])
    print(f"💎 Most savings: {most_savings['store']} - ₹{most_savings['savings']:.2f}")
    
    if results[0]['store'] == fastest['store']:
        print("✅ Best deal is also the fastest!")
    
    print("\n" + "="*70)
    
    print("\n📊 DETAILED CALCULATION FOR BEST OFFER:")
    print("-"*70)
    calc = results[0]['calculation']
    print(f"1. Original Price:     ₹{calc['original_price']:.2f}")
    print(f"2. Discount:           -₹{calc['discount_amount']:.2f}")
    print(f"3. After Discount:      ₹{calc['after_discount']:.2f}")
    print(f"4. Coupon:             -₹{calc['coupon_discount']:.2f}")
    print(f"5. After Coupon:        ₹{calc['after_coupon']:.2f}")
    print(f"6. Tax:                +₹{calc['tax_amount']:.2f}")
    print(f"7. After Tax:           ₹{calc['after_tax']:.2f}")
    print(f"8. Delivery:           +₹{calc['delivery_fee']:.2f}")
    print(f"9. Price Per Item:      ₹{calc['final_price']:.2f}")
    print(f"10. Quantity:           ×{calc['quantity']}")
    print(f"11. TOTAL FINAL PRICE:  ₹{calc['total_price']:.2f}")
    print(f"12. Total Savings:      ₹{calc['total_savings']:.2f}")
    
    print("\n📊 DETAILED CALCULATION FOR MOST EXPENSIVE OFFER:")
    print("-"*70)
    calc = results[-1]['calculation']
    print(f"1. Original Price:     ₹{calc['original_price']:.2f}")
    print(f"2. Discount:           -₹{calc['discount_amount']:.2f}")
    print(f"3. After Discount:      ₹{calc['after_discount']:.2f}")
    print(f"4. Coupon:             -₹{calc['coupon_discount']:.2f}")
    print(f"5. After Coupon:        ₹{calc['after_coupon']:.2f}")
    print(f"6. Tax:                +₹{calc['tax_amount']:.2f}")
    print(f"7. After Tax:           ₹{calc['after_tax']:.2f}")
    print(f"8. Delivery:           +₹{calc['delivery_fee']:.2f}")
    print(f"9. Price Per Item:      ₹{calc['final_price']:.2f}")
    print(f"10. Quantity:           ×{calc['quantity']}")
    print(f"11. TOTAL FINAL PRICE:  ₹{calc['total_price']:.2f}")
    print(f"12. Total Savings:      ₹{calc['total_savings']:.2f}")

def analyze_deals(results):
    print("\n📈 DEAL ANALYSIS:")
    print("-"*70)
    
    highest_discount = max(results, key=lambda x: x['offer']['discount_percent'])
    print(f"📊 Highest Discount: {highest_discount['store']} - {highest_discount['offer']['discount_percent']}%")
    
    prices = [r['final_price'] for r in results]
    print(f"📊 Price Range: ₹{min(prices):.2f} - ₹{max(prices):.2f}")
    print(f"📊 Price Difference: ₹{max(prices) - min(prices):.2f}")
    
    print("\n🔍 DECEPTIVE DISCOUNT CHECK:")
    for result in results:
        discount = result['offer']['discount_percent']
        final_price = result['final_price']
        original_price = result['offer']['original_price']
        effective_savings = ((original_price - final_price) / original_price) * 100
        
        if discount > 20 and effective_savings < discount - 10:
            print(f"⚠️ {result['store']}: {discount}% discount advertised")
            print(f"   But only {effective_savings:.1f}% actual savings")
            print(f"   Final price: ₹{final_price:.2f} vs original ₹{original_price:.2f}")
            print()
    
    if results[0]['offer']['discount_percent'] < results[-1]['offer']['discount_percent']:
        print("💡 Remember: Highest discount doesn't always mean lowest final price!")
        print(f"   {results[-1]['store']} has {results[-1]['offer']['discount_percent']}% discount")
        print(f"   But {results[0]['store']} is cheaper at ₹{results[0]['final_price']:.2f}")

def main():
    print("\n" + "="*70)
    print("     🏷️  ONLINE SHOPPING OFFER COMPARATOR")
    print("="*70)
    
    print("\nWelcome! This tool helps you find the best deal.")
    print("It calculates the true price after discounts, coupons, tax, and delivery.")
    
    print("\nHow would you like to compare?")
    print("1. Use sample offers (demo)")
    print("2. Enter your own offers")
    
    choice = input("\nEnter 1 or 2: ").strip()
    
    if choice == '2':
        offers = get_user_offers()
        if not offers:
            print("\nNo offers entered. Using sample data instead.")
            offers = get_sample_offers()
    else:
        offers = get_sample_offers()
    
    print(f"\n📦 Comparing {len(offers)} offers...")
    results = compare_offers(offers)
    display_results(results)
    analyze_deals(results)
    
    print("\n" + "="*70)
    print("✅ Comparison complete! Happy shopping! 🎉")
    print("="*70)

if __name__ == "__main__":
    main()