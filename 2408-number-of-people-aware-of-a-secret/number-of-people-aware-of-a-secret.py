class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        #key = day person learned secret, value = number of people  who learned on that day
        SecretsKnown = {1: 1}  # day 1 -> 1 person knows

        for i in range(2, n + 1):
            next_person = 0
            remove_person = []

            for learned_day, count in list(SecretsKnown.items()):
                # forgetting condition
                if i == learned_day + forget:
                    remove_person.append(learned_day)
                    continue

                # sharing condition
                if learned_day + delay <= i < learned_day + forget:
                    next_person = (next_person + count) % MOD

            # remove people who forgot
            for person in remove_person:
                SecretsKnown.pop(person)

            # add new people who learned today
            if next_person > 0:
                SecretsKnown[i] = (SecretsKnown.get(i, 0) + next_person) % MOD

        return sum(SecretsKnown.values()) % MOD