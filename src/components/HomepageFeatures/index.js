import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Who We Are',
    Svg: require('@site/static/img/logo.svg').default,
    description: (
      <>
        Redback is a capstone project company within Deakin University. Students work on Redback's projects under the guidance of professional and academic mentors.
      </>
    ),
  },
  {
    title: 'For Students',
    Svg: require('@site/static/img/docs.svg').default,
    description: (
      <>
        We are in the process of moving documentation here. <br></br><br></br>
        
        You'll hopefully be able to find documentations for all projects here, as well as general company things. Feel free to add / edit as neccessary within reason of your project.
      </>
    ),
  },
  {
    title: 'Our Statement',
    Svg: require('@site/static/img/question.svg').default,
    description: (
      <>
        Redback Operations is on a mission to transform small steps in the virtual world into significant strides in reality. Our goal is to make you Smarter, Fitter, and Better by adding an element of enjoyment to physical activity. We specialize in developing cutting-edge connected fitness devices designed to enhance the quality of exercise and the effectiveness of training. as well as using different sensor technologies to prevent the risk of injury.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
