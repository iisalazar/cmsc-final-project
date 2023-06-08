from db import db
from entities.Person import Person
from typing import List, Tuple
from entities.Transaction import Transaction


class BalanceService:
    def get_current_balance(self) -> int:
        cursor = db.cursor()
        cursor.execute(
            """
SELECT 
  borrowerAmount - lenderAmount AS balance 
FROM 
  (
    SELECT 
      (
        SELECT 
          SUM(
            CASE WHEN t.type = "payment" then - t.amount ELSE t.amount END
          ) 
        FROM 
          person AS p 
          INNER JOIN transaction AS t ON t.lendeeId = p.id 
        WHERE 
          p.isUser = 1 
        GROUP BY 
          p.id
      ) AS borrowerAmount, 
      (
        SELECT 
          SUM(
            CASE WHEN t.type = "payment" then - t.amount ELSE t.amount END
          ) 
        FROM 
          person AS p 
          INNER JOIN transaction AS t ON t.lenderId = p.id 
        WHERE 
          p.isUser = 1 
        GROUP BY 
          p.id
      ) AS lenderAmount
  ) AS subquery;

        """
        )
        result = cursor.fetchone()
        balance = result[0]

        cursor.close()
        return balance

    def get_friends_with_balance(self) -> List[Person]:
        raise NotImplementedError("Not implemented yet")

    def get_groups_with_outstanding_balance(self) -> List[Tuple[int, int]]:
        cursor = db.cursor()
        cursor.execute(
            """
	SELECT 
	expense.grpId, 
	expense.expense_total - payment.payment_total AS outstanding_balance
	FROM 
	  (
	    SELECT grpId, SUM(amount) AS expense_total
	    FROM transaction
	    WHERE grpId IS NOT NULL AND type = 'expense'
	    GROUP BY grpId
	    HAVING expense_total > 0
	  ) as expense 
	  INNER JOIN (
	    SELECT grpId, SUM(amount) AS payment_total
	    FROM transaction
	    WHERE grpId IS NOT NULL AND type = 'payment'
	    GROUP BY grpId
	    HAVING payment_total > 0
	  ) as payment ON expense.grpId = payment.grpId
	WHERE
	  expense.expense_total - payment.payment_total > 0;
"""
        )
        rows = cursor.fetchall()
        result: List[Tuple[int, int]] = []
        cursor.close()

        for row in rows:
            result.append((row[0], row[1]))

        return result
