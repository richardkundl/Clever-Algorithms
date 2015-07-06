using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CleverAlgorithms.Core.Stochastic
{
	public class RandomSearch
	{
		private int[] RandomFunction(int[] minMax) {
			return minMax;
		}

		private int[] ObjectiveFunction(int[] vector) {
			return vector;
		}

		public T Search<T>(int[] searchSpace, int iteration)
		{
			/*
			def objective_function(vector)
				return vector.inject(0) {|sum, x| sum + (x ** 2.0)}
			end

			def random_vector(minmax)
				return Array.new(minmax.size) do |i|
				minmax[i][0] + ((minmax[i][1] - minmax[i][0]) * rand())
				end
			end

			def search(search_space, max_iter)
				best = nil
				max_iter.times do |iter|
				candidate = {}
				candidate[:vector] = random_vector(search_space)
				candidate[:cost] = objective_function(candidate[:vector])
				best = candidate if best.nil? or candidate[:cost] < best[:cost]
				puts " > iteration=#{(iter+1)}, best=#{best[:cost]}"
				end
				return best
			end
			 */

			var best = 0.0;
			for (var iter = 0; iter < iteration; iter++)
			{
				var candidate = new { };
				var vector = RandomFunction(searchSpace);
				var cost = ObjectiveFunction(vector);

			}

			return default(T);
		}
	}
}
