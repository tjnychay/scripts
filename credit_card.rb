class Credit_card

### takes the limit and apr as inputs
  def initialize(limit, apr)
    @limit = limit
    @apr = apr
  end

  def calc_interest
  	credit = @limit
  	sum = 0
  	start_day = 0
  	total_interest = 0.00
  	amount_owed = 0.00
### what actions do you want to take for the user
    loop do
      puts "Would you like to [withdraw] or [make_payment] or [do_nothing]?"
      response = gets.chomp
      change = 0
      case response.downcase
### if withdraw then lowers the sum, but does not let you exceed your balance
	  when 'withdraw'
        puts "How much would you like to withdraw?"
        temp = gets.chomp.to_i
        if ((temp + sum.abs) > @limit)
          print "The withdrawal is too large, it exceeds your credit amount. "
        else
          change =- temp
        end

      when 'make_payment'
        puts "How much would you like to pay?"
        temp = gets.chomp.to_i
        if ((temp + sum) > 0)
          print "The payment is too large, it is over the credit limit. "
        else
          change =+ temp
        end

      when 'do_nothing'
        break

      else
      	print "Not a valid response. "
      	next
      end
      sum = sum + change
      if (sum < 0)
	    puts "what is the current day (0-30), where 0 is day one?"
        answer = gets.chomp.to_i
        if (@limit + sum) < @limit
      	  interest = sum.abs * @apr / 365 * (30 - answer)
      	  print interest
        end
        start_day = answer
        total_interest = total_interest + interest
      else
      	total_interest = 0.00
      end
    end
    amount_owed = total_interest + sum.abs
    credit = credit + sum
    print "Your 30 day payment amount is:", amount_owed
  end

end

#############

Credit_card.new(1000, 0.35).calc_interest