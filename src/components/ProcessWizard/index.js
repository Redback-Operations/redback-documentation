import React, { useState, useMemo } from 'react';
import styles from './ProcessWizard.module.css';
import MDXContent from '@theme/MDXContent';

export function ProcessWizard({ children }) {
    const [currentStep, setCurrentStep] = useState(0);
    const steps = useMemo(() => {
        return children.map(child => child.props.title);
    }, [children]);

    return (
        <div className={styles.processWizard}>
            <ProcessWizardProgressBar steps={steps} currentStep={currentStep} />
            <div className={styles.processWizardContent}>
                {React.cloneElement(children[currentStep], { stepNo: currentStep + 1 })}
                <div className={styles.processWizardNavButtons}>
                    {currentStep > 0 &&
                        <button onClick={() => setCurrentStep(currentStep - 1)}>
                            <span>&larr; </span>
                            Previous step
                        </button>
                    }
                    {currentStep < children.length - 1 &&
                        <button onClick={() => setCurrentStep(currentStep + 1)}>
                            Next step
                            <span>&rarr;</span>
                        </button>
                    }
                </div>
            </div>
        </div>
    );
}

export function ProcessWizardStep({ title, stepNo, children }) {

    return (
        <div className={styles.processWizardStep}>
            <h3>Step {stepNo}. {title}</h3>
            {children}
        </div>
    );
}

function ProcessWizardProgressBar({ steps, currentStep }) {
    return (
        <nav>
            <div className={styles.progressBar} style={{ width: `${(currentStep / steps.length) * 100}%` }} />
            <ol className={styles.progressBarItems}>
                {steps.map((step, index) => (
                    <li key={index} className={styles.progressBarItem} data-current={index === currentStep} data-passed={index < currentStep}>
                        {step}
                    </li>
                ))}
            </ol>
        </nav>
    );
}